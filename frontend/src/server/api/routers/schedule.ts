import { z } from "zod";

import {
    createTRPCRouter,
    protectedProcedure,
    publicProcedure,
} from "~/server/api/trpc";

export const scheduleRouter = createTRPCRouter({
    upload_ics: protectedProcedure
        .input(z.object({
            userId: z.number(),
            ics: z.string()
        }))
        .query(async ({ ctx , input }) => {
            await ctx.client.post(`/users/${input.userId}/schedule/ics`, input.ics);
        }),

    get_schedule: protectedProcedure
        .input(z.object({
            userId: z.number()
        }))
        .query(async ({ ctx, input }) => {
            const res = await ctx.client.get(`/users/${input.userId}/schedule`);

            const schema = z.object({
                name: z.string(),
                days: z.string().array(),
                start: z.string(),
                end: z.string()
            });

            const result = await schema.safeParseAsync(res.data);

            if (result.success) return result.data;
        }),
});
