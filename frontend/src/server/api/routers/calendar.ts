import { z } from "zod";

import {
  createTRPCRouter,
  protectedProcedure,
  publicProcedure,
} from "~/server/api/trpc";

export const calendarRouter = createTRPCRouter({
  import: publicProcedure
    .input(
      z.object({
        file: z.string(),
      }),
    )
    .mutation(async ({ ctx, input }) => {
      console.log(input.file);
    }),

  get: protectedProcedure.query(async ({ ctx, input }) => {
    const data = [
      {
        name: "",
        days: [""],
        location: "",
        start: "",
        end: "",
      },
    ];

    const schema = z
      .object({
        name: z.string(),
        days: z.string().array(),
        location: z.string(),
        start: z.string(),
        end: z.string(),
      })
      .array();

    await schema.parseAsync(data);

    return null;
  }),
});
