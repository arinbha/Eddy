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
        file: z.custom<File>(),
      }),
    )
    .mutation(({ ctx, input }) => {
      input.file;
    }),
});
